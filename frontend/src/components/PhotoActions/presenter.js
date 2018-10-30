import React from "react";
import PropTypes from "prop-types"
import Ionicon from "react-ionicons"
import styles from "./styles.module.scss"

const PhotoActions = (props, context) => {
    console.log(props)
    return (
        <div className={styles.actions}>
            <div className={styles.icons}>
                <span className={styles.icon}>
                    <Ionicon icon="ios-heart-outline" fontSize="20px" color="black"/>
                </span>
                <span className={styles.icon}>
                    <Ionicon icon="ios-text-outline" fontSize="20px" color="black"/>
                </span>
            </div>
            <span className={styles.likes}>
                    {props.number} {" "} {props.number === 1 
                    ? context.t("like") 
                    : context.t("likes") } 
            </span>
        </div>
    )
}
PhotoActions.contextTypes = {
    t : PropTypes.func.isRequired
}

PhotoActions.propTypes = {
    number: PropTypes.number.isRequired
}

export default PhotoActions;
