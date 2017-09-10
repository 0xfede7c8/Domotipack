import React, { Component } from 'react'

export default class Alarm extends Component{
    render(){
        return (
            <div>
                <h3>ALARM</h3>
                <div className="row">
                    <div className="col-md-6">
                        ENABLE
                    </div>
                    <div className="col-md-6">
                        <label className="mdl-switch mdl-js-switch mdl-js-ripple-effect">
                            <input type="checkbox" className="mdl-switch__input"/>
                            <span className="mdl-switch__label"></span>
                        </label>
                    </div>
                </div>
            </div>
        );
    }
}
