import React, { Component } from 'react';
import DevicesList from '../containers/devicesList'

class App extends Component {
  render() {
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
}

export default App;
