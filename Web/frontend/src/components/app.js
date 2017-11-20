import React from 'react';
import DevicesList from './devices/devicesList'

export default (props)=>{
    return (
        <div className="container-fluid">
            <div className="row">
                <div className="col-md-2"></div>
                <div className="col-md-8">
                    <DevicesList />
                </div>
                <div className="col-md-2"></div>
            </div>
        </div>
   );
}

