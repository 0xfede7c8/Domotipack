import React, { Component } from 'react'

export default class THSensor extends Component {

    render(){
        return (
            <div>
                <div className="row">
                    <div className="col-md-4">
                       Temperature: 
                         <h3> <i>
                          {this.props.device.state.TC} ºC
                        </i></h3>
                    </div>
                    <div className="col-md-4">
                        Humidity:
                        <h3> <i>
                            {this.props.device.state.H} %
                        </i></h3>
                    </div>
                </div>
            </div>
        );
    }
}
