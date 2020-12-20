function sysCall_init()

    --Assign Object Handle Variables for Ropes and Joints
    J1=sim.getObjectHandle('rope1')
    J2=sim.getObjectHandle('rope2')
    J3=sim.getObjectHandle('rope3')
    J4=sim.getObjectHandle('rope4')
    FJ1=sim.getJointForce(J1)
    FJ2=sim.getJointForce(J2)
    FJ3=sim.getJointForce(J3)
    FJ4=sim.getJointForce(J4)
    
    --Popup window text for Joint Positions and Joint Forces
    xml = 
    [[
        <ui title="AgBot Control" closeable="true" resizable="false" activate="false">
             <group layout="vbox" flat="true">
                <label text="<big> Joint Forces: </big>" wordwrap="false" style="font-weight: bold;"/>
                <label text="Joint 1 Position (m): 0.10" id="1"/>
                <hslider tick-position="above" tick-interval="1" minimum="-10" maximum="10" on-change="ActuateL1" id="2"/>
                <label text="Joint 2 Position (m): 0.10" id="3"/>
                <hslider tick-position="above" tick-interval="1" minimum="-10" maximum="10" on-change="ActuateL2" id="4"/>
                <label text="Joint 3 Position (m): 0.10" id="5"/>
                <hslider tick-position="above" tick-interval="1" minimum="-10" maximum="10" on-change="ActuateL3" id="6"/>
                <label text="Joint 4 Position (m): 0.10" id="7"/>
                <hslider tick-position="above" tick-interval="1" minimum="-10" maximum="10" on-change="ActuateL4" id="8"/>
             </group>
             
             <group layout="vbox" flat="true">
                <label text="<big> Joint Forces: </big>" wordwrap="false" style="font-weight: bold;"/>
                <label text="Force on Joint 1: " id="9" />
                <label text="Force on Joint 2: " id="10" />
                <label text="Force on Joint 3: " id="11" />
                <label text="Force on Joint 4: " id="12" />
             </group>
             <label text="" style="* {margin-left: 400px;}"/>
        </ui>
    ]]
        ui=simUI.create(xml)
        -- Initial values used when starting the simulation
        simUI.setSliderValue(ui,2,1)
        simUI.setSliderValue(ui,4,1)
        simUI.setSliderValue(ui,6,1)
        simUI.setSliderValue(ui,8,1)
        simUI.setLabelText(ui,9,string.format("Force on Joint 1 (N): %.2f",PJ1))
        simUI.setLabelText(ui,10,string.format("Force on Joint 2 (N): %.2f",PJ2))
        simUI.setLabelText(ui,11,string.format("Force on Joint 3 (N): %.2f",PJ3))
        simUI.setLabelText(ui,12,string.format("Force on Joint 4 (N): %.2f",PJ4))
    end
    
    --Link 1 Actuator Function
    function ActuateL1(ui,id,NewValue)
        local ScaledValue = .1 * NewValue
        local ForceValue=sim.getJointForce(J1) -- Gets the force on the respective joints along the z-axis (active axis)
        sim.setJointTargetPosition(J1,ScaledValue)
        simUI.setLabelText(ui,1,string.format("Joint 1 Position (m): %.2f",ScaledValue))
        simUI.setLabelText(ui,9,string.format("Force on Joint 1 (N): %.2f",ForceValue))
    
    end
    
    --Link 2 Actuator Function
    function ActuateL2(ui,id,NewValue)
        local ForceValue=sim.getJointForce(J2)
        local ScaledValue = .1 * NewValue
        sim.setJointTargetPosition(J2,ScaledValue)
        simUI.setLabelText(ui,3,string.format("Joint 2 Position (m): %.2f",ScaledValue))    
        simUI.setLabelText(ui,10,string.format("Force on Joint 2 (N): %.2f",ForceValue))
    
    end
    
    --Link 3 Actuator Function
    function ActuateL3(ui,id,NewValue)
        local ForceValue=sim.getJointForce(J3)
        local ScaledValue = .1 * NewValue
        sim.setJointTargetPosition(J3,ScaledValue)
        simUI.setLabelText(ui,5,string.format("Joint 3 Position (m): %.2f",ScaledValue))
        simUI.setLabelText(ui,11,string.format("Force on Joint 3 (N): %.2f",ForceValue))
    end
    
    --Link 4 Actuator Function
    function ActuateL4(ui,id,NewValue)
        local ForceValue=sim.getJointForce(J4)
        local ScaledValue = .1 * NewValue
        sim.setJointTargetPosition(J4,ScaledValue)
        simUI.setLabelText(ui,7,string.format("Joint 4 Position (m): %.2f",ScaledValue))
        simUI.setLabelText(ui,12,string.format("Force on Joint 4 (N): %.2f",ForceValue))
    end
    
    function sysCall_actuation()
        -- put your actuation code here
    end
    
    function sysCall_sensing()
        -- put your sensing code here
    end
    
    function sysCall_cleanup()
        -- do some clean-up here
    end
