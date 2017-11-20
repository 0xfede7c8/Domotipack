import React, { Component } from 'react'
import Toggle from 'material-ui/Toggle'

export default class Alarm extends Component {
    render(){
        return (
            <div>
                <div className="row">
                    <div className="col-md-6">
                        ENABLE
                    </div>
                    <div className="col-md-6">
                        <Toggle />
                    </div>
                </div>
            </div>
        );
    }
}
