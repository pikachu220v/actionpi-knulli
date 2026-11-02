from pathlib import Path
r=Path('work/flycast-vk');p=r/'source/core/rend/vulkan/vulkan_context.cpp';t=p.read_text()
if 'ACTIONPI_STANDALONE_DIRECT_DISPLAY' not in t:
    head='bool VulkanContext::init()\n'
    assert t.count(head)==1
    t=t.replace(head,'#include "actionpi_display.h" // ACTIONPI_STANDALONE_DIRECT_DISPLAY\n\n'+head)
    old='''    uint32_t extensionsCount = 0;
    SDL_Vulkan_GetInstanceExtensions((SDL_Window *)window, &extensionsCount, NULL);
    extensions.resize(extensionsCount + extensions.size());
    SDL_Vulkan_GetInstanceExtensions((SDL_Window *)window, &extensionsCount, &extensions[extensions.size() - extensionsCount]);'''
    assert t.count(old)==1
    t=t.replace(old,'\textensions.push_back(vk::KHRDisplayExtensionName);')
    old='if (SDL_Vulkan_CreateSurface((SDL_Window *)window, (VkInstance)*instance, &surface) == 0)'
    assert t.count(old)==1
    t=t.replace(old,'if (!actionpiCreateDisplaySurface((VkInstance)*instance, &surface))')
    p.write_text(t)
(p.parent/'actionpi_display.h').write_bytes((r/'actionpi_display.h').read_bytes())
print('Display source patch ready')
