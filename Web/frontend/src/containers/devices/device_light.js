import React, { Component } from 'react'

export default class Light extends Component{
    handleSlider(){
        const slider = document.getElementById("light-slider");
        console.log("slider change")
    }
    render(){
        return (
            <div>
                <h3>LIGHT</h3>
                <div className="row">
                    <div className="col-md-6">
                        ON/OFF:
                    </div>
                    <div className="col-md-6">
                        <label className="mdl-switch mdl-js-switch mdl-js-ripple-effect">
                            <input type="checkbox" className="mdl-switch__input"/>
                            <span className="mdl-switch__label"></span>
                        </label>
                    </div>
                </div>
                <div className="row">
                    <div className="col-md-12">
                        <input onChange={this.handleSlider} id="light-slider" className="mdl-slider mdl-js-slider" type="range"
                        min="0" max="100" value="0" tabIndex="0" />
                    </div>
                </div>
            </div>
        );
    }
}

