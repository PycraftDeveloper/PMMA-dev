#include "Display.hpp"
#include "PMMA_Core.hpp"

static CPP_Display* display_instance = nullptr;
static bool GLFW_Initialized = false;
static int GLFW_References = 0;

extern "C" {

EXPORT CPP_Display* GetDisplayInstance() {
    return display_instance;
}

EXPORT void SetDisplayInstance(CPP_Display* new_instance) {
    display_instance = new_instance;
}

EXPORT bool Get_GLFW_Initialized() {
    return GLFW_Initialized;
}

EXPORT void Set_GLFW_Initialized(bool value) {
    GLFW_Initialized = value;
}

EXPORT int Get_GLFW_References() {
    return GLFW_References;
}

EXPORT void Set_GLFW_References(int value) {
    GLFW_References = value;
}

}