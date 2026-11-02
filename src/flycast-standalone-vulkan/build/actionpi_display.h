/* Action Pi standalone trial only: select the logical mode exposed by the
 * existing scoped Vulkan rotation loader, without SDL's physical-window-size
 * mode filter. No kernel, shared SDL, or display-driver changes. */
static bool actionpiCreateDisplaySurface(VkInstance instance, VkSurfaceKHR *surface)
{
    auto gi = VULKAN_HPP_DEFAULT_DISPATCHER.vkGetInstanceProcAddr;
    auto enumerate = reinterpret_cast<PFN_vkEnumeratePhysicalDevices>(gi(instance, "vkEnumeratePhysicalDevices"));
    auto displays = reinterpret_cast<PFN_vkGetPhysicalDeviceDisplayPropertiesKHR>(gi(instance, "vkGetPhysicalDeviceDisplayPropertiesKHR"));
    auto modes = reinterpret_cast<PFN_vkGetDisplayModePropertiesKHR>(gi(instance, "vkGetDisplayModePropertiesKHR"));
    auto planes = reinterpret_cast<PFN_vkGetPhysicalDeviceDisplayPlanePropertiesKHR>(gi(instance, "vkGetPhysicalDeviceDisplayPlanePropertiesKHR"));
    auto supported = reinterpret_cast<PFN_vkGetDisplayPlaneSupportedDisplaysKHR>(gi(instance, "vkGetDisplayPlaneSupportedDisplaysKHR"));
    auto caps = reinterpret_cast<PFN_vkGetDisplayPlaneCapabilitiesKHR>(gi(instance, "vkGetDisplayPlaneCapabilitiesKHR"));
    auto create = reinterpret_cast<PFN_vkCreateDisplayPlaneSurfaceKHR>(gi(instance, "vkCreateDisplayPlaneSurfaceKHR"));
    if (!enumerate || !displays || !modes || !planes || !supported || !caps || !create)
        return false;
    uint32_t count = 0;
    if (enumerate(instance, &count, nullptr) != VK_SUCCESS || count == 0) return false;
    std::vector<VkPhysicalDevice> devices(count);
    if (enumerate(instance, &count, devices.data()) != VK_SUCCESS) return false;
    for (auto gpu : devices) {
        uint32_t nd = 0;
        if (displays(gpu, &nd, nullptr) != VK_SUCCESS || nd == 0) continue;
        std::vector<VkDisplayPropertiesKHR> ds(nd);
        if (displays(gpu, &nd, ds.data()) != VK_SUCCESS) continue;
        uint32_t np = 0;
        if (planes(gpu, &np, nullptr) != VK_SUCCESS || np == 0) continue;
        std::vector<VkDisplayPlanePropertiesKHR> ps(np);
        if (planes(gpu, &np, ps.data()) != VK_SUCCESS) continue;
        for (auto &display : ds) {
            uint32_t nm = 0;
            if (modes(gpu, display.display, &nm, nullptr) != VK_SUCCESS || nm == 0) continue;
            std::vector<VkDisplayModePropertiesKHR> ms(nm);
            if (modes(gpu, display.display, &nm, ms.data()) != VK_SUCCESS) continue;
            for (auto &mode : ms) {
                if (mode.parameters.visibleRegion.width != 960 || mode.parameters.visibleRegion.height != 720) continue;
                for (uint32_t plane = 0; plane < np; ++plane) {
                    if (ps[plane].currentDisplay && ps[plane].currentDisplay != display.display) continue;
                    uint32_t ns = 0;
                    if (supported(gpu, plane, &ns, nullptr) != VK_SUCCESS || ns == 0) continue;
                    std::vector<VkDisplayKHR> supportedDisplays(ns);
                    if (supported(gpu, plane, &ns, supportedDisplays.data()) != VK_SUCCESS) continue;
                    if (std::find(supportedDisplays.begin(), supportedDisplays.end(), display.display) == supportedDisplays.end()) continue;
                    VkDisplayPlaneCapabilitiesKHR limits{};
                    if (caps(gpu, mode.displayMode, plane, &limits) != VK_SUCCESS) continue;
                    if (!(display.supportedTransforms & VK_SURFACE_TRANSFORM_IDENTITY_BIT_KHR)) continue;
                    VkDisplayPlaneAlphaFlagBitsKHR alpha = VK_DISPLAY_PLANE_ALPHA_OPAQUE_BIT_KHR;
                    if (!(limits.supportedAlpha & alpha)) {
                        alpha = VK_DISPLAY_PLANE_ALPHA_GLOBAL_BIT_KHR;
                        if (!(limits.supportedAlpha & alpha)) continue;
                    }
                    VkDisplaySurfaceCreateInfoKHR info{};
                    info.sType = VK_STRUCTURE_TYPE_DISPLAY_SURFACE_CREATE_INFO_KHR;
                    info.displayMode = mode.displayMode;
                    info.planeIndex = plane;
                    info.planeStackIndex = ps[plane].currentStackIndex;
                    info.transform = VK_SURFACE_TRANSFORM_IDENTITY_BIT_KHR;
                    info.globalAlpha = 1.f;
                    info.alphaMode = alpha;
                    info.imageExtent = mode.parameters.visibleRegion;
                    VkResult result = create(instance, &info, nullptr, surface);
                    fprintf(stderr, "ACTIONPI_STANDALONE_VK display logical=960x720 refresh=%u plane=%u result=%d\n", mode.parameters.refreshRate, plane, result);
                    if (result == VK_SUCCESS) return true;
                }
            }
        }
    }
    return false;
}
