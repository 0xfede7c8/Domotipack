import React, { Component } from 'react';
import Slider from 'material-ui/Slider';
import Toggle from 'material-ui/Toggle';

export default class Light extends Component{
    
    constructor(props){
        super(props);
        this.state = {
            slider_enabled : props.device.state.on
        }
    }

    handleSliderDivClick(event){
        this.setState({slider_enabled: true});
    }

    handleSlider(event, new_value){
        var not_zero = new_value != 0
        const device_state= Object.assign(this.props.device.state,
            {value:new_value, on:not_zero});
        const device = Object.assign(this.props.device,{state: device_state});
        this.props.onStateChange(this.props.device);
    }

    handleToggle(event, is_checked){
        this.setState({slider_enabled: is_checked});
        const device_state= Object.assign(this.props.device.state, {on:is_checked});
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
                    <div className="col-md-12" onClick={this.handleSliderDivClick.bind(this)}>
                        <Slider 
                            onChange={this.handleSlider.bind(this)}
                            value = {this.props.device.state.value}
                            disabled = {this.state.slider_enabled}
                            max = {100}
                            step = {1}
                        />
                    </div>
                </div>
            </div>
        );
    }
}

