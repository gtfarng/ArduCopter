#!/usr/bin/env python
# encoding: utf-8

def build(bld):
    vehicle = bld.path.name
    bld.ap_stlib(
        name=vehicle + '_libs',
        ap_vehicle=vehicle,
        ap_libraries=bld.ap_common_vehicle_libraries() + [
            'AP_ADSB',
            'AC_AttitudeControl',
            'AC_InputManager',
            'AC_Fence',
            'AC_Avoidance',
            'AC_PID',
            'AC_PrecLand',
            'AC_Sprayer',
            'AC_WPNav',
            'AP_Camera',
            'AP_IRLock',
            'AP_InertialNav',
            'AP_LandingGear',
            'AP_Menu',
            'AP_Motors',
            'AP_Parachute',
            'AP_RCMapper',
            'AP_Avoidance',
            'AP_AdvancedFailsafe',
            'AP_Proximity',
            'AP_SmartRTL',
            'AP_Stats',
            'AP_Gripper',
            'AP_Beacon',
            'AP_Arming',
            'AP_VisualOdom',
            'AP_WheelEncoder',
            'AP_Winch',
        ],
    )

    bld.ap_program(
        program_name='arducopter',
        program_groups=['bin', 'copter'],
        use=vehicle + '_libs',
        defines=['FRAME_CONFIG=MULTICOPTER_FRAME'],
        )

    bld.ap_program(
        program_name='arducopter-heli',
        program_groups=['bin', 'copter'],
        use=vehicle + '_libs',
        defines=['FRAME_CONFIG=HELI_FRAME'],
        )
