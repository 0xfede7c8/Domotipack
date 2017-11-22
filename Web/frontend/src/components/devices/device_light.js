import React, { Component } from 'react';
import Slider from 'material-ui/Slider';
import Toggle from 'material-ui/Toggle';

export default class Light extends Component{

    handleSlider(event, new_value){
        var not_zero = new_value != 0
        const device_state= Object.assign(this.props.device.state,
            {value:new_value, on:not_zero});
        const device = Object.assign(this.props.device,{state: device_state});
        this.props.onStateChange(this.props.device);
    }

    handleToggle(event, is_checked){
        var new_value;
        if (is_checked){new_value = 100;}
        else{new_value = 0;}
        this.props.device.state.value = new_value;
        const device_state= Object.assign(this.props.device.state,
            {value: new_value, on:is_checked});
        const device = Object.assign(this.props.device,{state: device_state});
        this.props.onStateChange(device);
    }

    //disabled = {/*!this.props.device.state.on*/}
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
                            disableFocusRipple = {!this.props.device.state.on}
                            max = {100}
                            step = {1}
                        />
                    </div>
                </div>
            </div>
        );
    }
}

