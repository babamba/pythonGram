import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { ConnectedRouter } from "react-router-redux";
import store, { history } from 'redux/configureStore';
import 'index.css';
import App from 'App';
import "ReactotronConfig"

// 라우터에게 히스토리 오브젝트를 전달
// 그래서 router , middleware 둘다 같은 동일한 히스토리 오브젝트를 갖게됨
ReactDOM.render(
    <Provider store = { store }>

        <ConnectedRouter history= { history } >
            <App />
        </ConnectedRouter>
    </Provider>,
     document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA


