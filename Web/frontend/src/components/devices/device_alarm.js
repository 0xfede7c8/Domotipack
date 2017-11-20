import React, { Component } from 'react'
import Toggle from 'material-ui/Toggle'

export default class Alarm extends Component {
    handleToggle(event, is_checked){
        const device_state = Object.assign(this.props.device.state, {armed:is_checked});
        const device = Object.assign(this.props.device,{state: device_state});
        this.props.onStateChange(device);
    }
    handleSlider(event, new_value){
        const device_state= Object.assign(this.props.device.state, {value:new_value});
        const device = Object.assign(this.props.device,{state: device_state});
        this.props.onStateChange(device);
    }

    render(){
        return (
            <div>
                <div className="row">
                    <div className="col-md-6">
                        ENABLE
                    </div>
                    <div className="col-md-6">
                        <Toggle 
                            onToggle={this.handleToggle.bind(this)}
                        />
                    </div>
                </div>
                <div className="row">
                    {this.props.device.state.active}
                </div>
            </div>
        );
    }
}
