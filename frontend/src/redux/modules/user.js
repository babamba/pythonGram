//imports

// actions

const SAVE_TOKEN = "SAVE_TOKEN";
const LOGOUT = "LOGOUT";

// action creators 리덕스 state 바꿀때 사용

//토큰을 받을때마다 받은 토큰과 함께 saveToken이라는 액션을 디스패치함. -> 해당 액션을 리듀서에 실행 
// -> 리듀서가  applySetToken() 을 실행하고 isLoggedIn은 참으로 하고 이를 state에 저장
function saveToken(token){
    return {
        type:SAVE_TOKEN,
        token
    }
}

function logout(){
    return {
        type: LOGOUT
    }
}

// API actions API부를 떄 사용

function facebookLogin(access_token){
    return function(dispatch){
        fetch("/users/login/facebook/", {
            method : "POST",
            headers:{
                "Content-Type": "application/json"
            },
            body : JSON.stringify({
                //access_token: access_token
                access_token
            })
        })
        .then(response => response.json())
        .then(json => {
             // request가 정상적으로 실행됬고 response json 안에 token이 있다
             // json을 인수로 받아 saveToken에 함께 보내준다 (보내주면 알아서 숙숙숙)
            if(json.token){
                dispatch(saveToken(json.token));
            }
        })
        .catch(err => console.log(err))

    }
}

function usernameLogin(username, password){
    return function(dispatch){
        fetch("/rest-auth/login/", {
            method : "POST",
            headers:{
                "Content-Type" : "application/json"
            },
            body : JSON.stringify({
                //access_token: access_token
                username,
                password
            })
        })
        .then(response => response.json())
        .then(json => {
            if(json.token){
                dispatch(saveToken(json.token))
            }
        })
        .catch(err => console.log(err))
    }
}

function createAccount(username, password, email, name){
    return function(dispatch){
        fetch("/rest-auth/registration/", {
            method : "POST",
            headers:{
                "Content-Type" : "application/json"
            },
            body : JSON.stringify({
                //access_token: access_token
                username,
                password1 : password,
                password2 : password,
                email,
                name
            })
        })
        .then(response => response.json())
        .then(json => {
            if(json.token){
                dispatch(saveToken(json.token))
            }
        })
    }
}

// initial state

const initialState = {
    isLoggedIn: localStorage.getItem("jwt") ? true : false,
    token : localStorage.getItem("jwt")
};

// reducer
function reducer(state = initialState, action ){
    switch(action.type){
        case SAVE_TOKEN:
            return applySetToken(state, action);
        case LOGOUT :
            return applyLogout(state, action);
            default:
        return state;
    }
}

// reducer functions

function applySetToken(state, action){
    const { token } = action;
    localStorage.setItem("jwt",token)
    return {
        ...state,
        isLoggedIn:true,
        token : token
    }
}

function applyLogout(state, action){
    localStorage.removeItem("jwt");
    return {
        isLoggedIn : false
    }
}

// exports

const actionCreators = {
    facebookLogin,
    usernameLogin,
    createAccount,
    logout
}

export { actionCreators };

// reducer export

export default reducer;