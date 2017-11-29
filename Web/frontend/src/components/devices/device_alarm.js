import React, { Component } from 'react'
import Dialog from 'material-ui/Dialog';
import Toggle from 'material-ui/Toggle'
import FlatButton from 'material-ui/FlatButton';


export default class Alarm extends Component {

    handleToggle(event, is_checked){
        const device_state = Object.assign(this.props.device.state, {armed:is_checked});
        const device = Object.assign(this.props.device,{state: device_state});
        this.props.onStateChange(device);
    }

    handleClose(){
        const device_state = Object.assign(this.props.device.state, {armed:false});
        const device = Object.assign(this.props.device,{state: device_state});
        this.props.onStateChange(device);
    }

    handleSlider(event, new_value){
        const device_state= Object.assign(this.props.device.state, {value:new_value});
        const device = Object.assign(this.props.device,{state: device_state});
        this.props.onStateChange(device);
    }

    render(){
    const actions = [
      <FlatButton
        label="Desactivar"
        primary={true}
        onClick={this.handleClose.bind(this)}
      />,
    ];
        return (
            <div>
                <div className="row">
                    <div className="col-md-6">
                        ENABLE
                    </div>
                    <div className="col-md-6">
                        <Toggle 
                            onToggle={this.handleToggle.bind(this)}
                            toggled={this.props.device.state.armed}
                        />
                    </div>
                </div>
        <Dialog
          title="Alarma Activada"
		  actions={actions}
          modal={true}
          open={this.props.device.state.active}
          onRequestClose={this.handleClose}
        >
        </Dialog>
            </div>
        );
    }
}
