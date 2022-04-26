import store from "../store/index"

export function keyMap(){
    const camerControl =  store.state.viewer.cameraControl;
    store.state.viewer.cameraControl.navMode = "firstPerson";
    const scene = store.state.viewer.scene;
    const keyMap = {};
    camerControl.followPointer = false;
    const input = scene.input;
    keyMap[camerControl.DOLLY_FORWARDS] = [input.KEY_UP_ARROW];
    keyMap[camerControl.DOLLY_BACKWARDS] = [input.KEY_DOWN_ARROW];
    keyMap[camerControl.PAN_LEFT] = [input.KEY_LEFT_ARROW];
    keyMap[camerControl.PAN_RIGHT] = [input.KEY_RIGHT_ARROW];
    keyMap[camerControl.PAN_UP] = [input.KEY_Z];
    keyMap[camerControl.PAN_DOWN] = [input.KEY_X];
    keyMap[camerControl.ROTATE_X_POS] = [input.KEY_R];
    keyMap[camerControl.ROTATE_X_NEG] = [input.KEY_T];
    keyMap[camerControl.ROTATE_Y_POS] = [input.KEY_Y];
    keyMap[camerControl.ROTATE_Y_NEG] = [input.KEY_U];
    keyMap[camerControl.AXIS_VIEW_RIGHT] = [input.KEY_NUM_1];
    keyMap[camerControl.AXIS_VIEW_BACK] = [input.KEY_NUM_2];
    keyMap[camerControl.AXIS_VIEW_LEFT] = [input.KEY_NUM_3];
    keyMap[camerControl.AXIS_VIEW_FRONT] = [input.KEY_NUM_4];
    keyMap[camerControl.AXIS_VIEW_TOP] = [input.KEY_NUM_5];
    keyMap[camerControl.AXIS_VIEW_BOTTOM] = [input.KEY_NUM_6];

    camerControl.keyMap = keyMap;
}