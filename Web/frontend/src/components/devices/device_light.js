import React, { Component } from 'react';
import Slider from 'material-ui/Slider';
import Toggle from 'material-ui/Toggle';

export default class Light extends Component{

    handleSlider(event, new_value){
        const device = Object.assign(this.props.device, {state: {value : new_value}});
        this.props.onStateChange(device);
    }

    handleToggle(event, is_checked){
        console.log(this.props.device);
    }

    render(){
        return (
            <div>
                <div className="row">
                    <div className="col-md-6">
                        ON/OFF:
                    </div>
                    <div className="col-md-6">
                        <Toggle onToggle={this.handleToggle.bind(this)}/>
                    </div>
                </div>
                <div className="row">
                    <div className="col-md-12">
                        <Slider 
                            onChange={this.handleSlider.bind(this)}
                            value = {this.props.device.state.value}
                            max = {100}
                            step = {1}
                        />
                    </div>
                </div>
            </div>
        );
    }
}

