import React, { Component } from 'react';
import Slider from 'material-ui/Slider';
import Toggle from 'material-ui/Toggle';

export default class Light extends Component{

    handleSlider(event, new_value){
        const device_state= Object.assign(this.props.device.state, {value:new_value});
        const device = Object.assign(this.props.device,{state: device_state});
        this.props.onStateChange(device);
    }

    handleToggle(event, is_checked){
        const device_state= Object.assign(this.props.device.state, {on:is_checked});
        const device = Object.assign(this.props.device,{state: device_state});
        this.props.onStateChange(device);
    }

    render(){
        return (
            <div>
                <div className="row">
                    <div className="col-md-6">
                        ON/OFF:
                    </div>
                    <div className="col-md-6">
                        <Toggle 
                            onToggle={this.handleToggle.bind(this)}
                            toggled= {this.props.device.state.on}
                        />
                    </div>
                </div>
                <div className="row">
                    <div className="col-md-12">
                        <Slider 
                            onChange={this.handleSlider.bind(this)}
                            value = {this.props.device.state.value}
                            disabled = {!this.props.device.state.on}
                            max = {100}
                            step = {1}
                        />
                    </div>
                </div>
            </div>
        );
    }
}

