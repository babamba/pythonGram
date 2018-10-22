import React, { Component } from 'react';
import styles from './styles.module.scss';
import Footer from "components/Footer";

//fetch('/notifications/')


class App extends Component {
  render() {
    return (
      <div className={styles.App}>
        <Footer />
      </div>
    );
  }
}

export default App;
