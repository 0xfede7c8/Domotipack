import React from 'react';
import Alarm from './device_alarm';
import Light from './device_light';
import THSensor from './device_thsensor';
import { Card, CardHeader, CardText} from 'material-ui/Card';

const LIGHT = 'light';
const ALARM = 'alarm';
const THSENSOR = 'thsensor';

export default function(props){
    var device;
    switch(props.device.type){
        case LIGHT:
            device = <Light 
                        device={props.device}
                        onStateChange = {props.onStateChange}
                    />;
            break;
        case ALARM:
            device = <Alarm
                        device={props.device}
                        onStateChange = {props.onStateChange}
                    />;
            break;
        case THSENSOR:
            device = <THSensor
                        device={props.device}
                        onStateChange = {props.onStateChange}
                    />;
            break;
        default:
            device = null;
            break;
    }

    return (
        <Card initiallyExpanded={true}>
            <CardHeader
                title={props.device.type.toUpperCase()}
                subtitle="description"
                actAsExpander={true}
                showExpandableButton={true}
            />
            <CardText expandable={true} style={{padding: "20px"}}>
                { device }
            </CardText>
        </Card>
    );
}
