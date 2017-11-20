import { combineReducers } from 'redux';
import DevicesList from './reducer_devices';

const rootReducer = combineReducers({
    devices : DevicesList
});
export default rootReducer;
