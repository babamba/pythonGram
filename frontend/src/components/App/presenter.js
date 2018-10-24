import React from 'react';
import PropTypes from "prop-types";
import { Route, Switch } from 'react-router-dom';
import './styles.module.scss';
import Footer from "components/Footer";
import Auth from "components/Auth";


//fetch('/notifications/')
// presenter 는 ui에 관련된 것을 갖고있다.
// props 에서 데이터가 나오고 로직 없고 오직 UI만 
// 프리젠터는 리덕스가 뭔지 모름 
console.log("App Presneter");

const App = props => [
  // Nav,
  props.isLoggedIn ? <PrivateRoutes key={2} /> : <PublicRoutes key={2} />,// Priv : // Public 
  <Footer key={3} />
]

App.propTypes = {
  isLoggedIn : PropTypes.bool.isRequired
};

const PrivateRoutes = props => (
  <Switch>
    <Route exact path ="/" render={() => "feed" }/>
    <Route exact path ="/explore" render={() => "explore" }/>
  </Switch>
);

const PublicRoutes = props => (
  <Switch>
    <Route exact path ="/" component={Auth}/>
    <Route exact path ="/forgot" render={() => "password" }/>
  </Switch>
);


// class App extends Component {
//   render() {
//     return (
//       <div className={styles.App}>
//         <Switch>
//           <Route apth="/" render={() => "hello!"} />
//           <Route apth="/login" render={() => "login!"} />
//         </Switch>
//         <Footer />
//       </div>
//     );
//   }
// }

export default App;
