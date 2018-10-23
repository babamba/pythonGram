//imports

// actions

// action creators

// initial state

const initialState = {
    isLoggedIn: localStorage.getItem("jwt") ? true : false,
    token: localStorage.getItem("jwt")
};

// reducer

function reducer(state = initialState, action ){
    switch(action.type){
        default:
        return state;
    }
}

// reducer functions

// exports

// reducer export

export default reducer;