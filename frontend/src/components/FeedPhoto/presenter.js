import React from "react";
import PropTypes from "prop-types"

import styles from "./styles.module.scss"

const FeedPhoto = (props, context) => {
    console.log(props)
    return <div className={styles.feedPhoto}>photo list </div>
}

FeedPhoto.propTypes = {
    // 오브젝트 일때 (내부안에 값이 있을때 ) shape 사용
    creator : PropTypes.shape({
        profile_image: PropTypes.string,
        username: PropTypes.string.isRequired
    }),
    location: PropTypes.string.isRequired,
    file: PropTypes.string.isRequired,
    like_count:PropTypes.number.isRequired,
    caption:PropTypes.string.isRequired,
    // 배열안의 오브젝트 
    commnet : PropTypes.arrayOf(
        PropTypes.shape({
            message : PropTypes.string.isRequired,
            creator : PropTypes.shape({
                profile_image: PropTypes.string,
                username: PropTypes.string.isRequired
            }).isRequired,
        })
    ),
    created_at : PropTypes.string.isRequired
}

export default FeedPhoto;
