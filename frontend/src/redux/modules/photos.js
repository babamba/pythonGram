//imports
import { actionCreators as userActions} from "redux/modules/user";
// actions

const SET_FEED = "SET_FEED";

// action creators 리덕스 state 바꿀때 사용

function setFeed(feed){
    return {
        type: SET_FEED,
        feed
    }
}

//토큰을 받을때마다 받은 토큰과 함께 saveToken이라는 액션을 디스패치함. -> 해당 액션을 리듀서에 실행 
// -> 리듀서가  applySetToken() 을 실행하고 isLoggedIn은 참으로 하고 이를 state에 저장


// API actions API부를 떄 사용

function getFeed(){
    return (dispatch, getState) => {
        const { user : { token } } = getState();
        fetch("/images/", {
            headers:{
                "Authorization" : `JWT ${token}`
            }
        })
        .then(response => {
            if(response.status === 401){
                dispatch(userActions.logout());
            }
            return response.json();
        })
        .then(json => dispatch(setFeed(json)))
    }
}

// initial state

const initialState = {};

// reducer

function reducer(state = initialState , action){
    switch(action.type){
        case SET_FEED:
            return applySetFeed(state, action)
        default:
            return state;
    }
}


// reducer functions

function applySetFeed(state, action){
    const { feed } = action;
    return {
        ...state,
        feed
    }
}

// exports

const actionCreators = {
    getFeed
}


export { actionCreators };

// reducer export

export default reducer;