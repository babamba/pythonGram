import React from "react";
import PropTypes from "prop-types"
import styles from "./styles.module.scss"
import PhotoActions from "../../components/PhotoActions"
import PhotoComments from "../../components/PhotoComments"
import TimeStamp from "../../components/TimeStamp"
import CommentBox from "../../components/CommentBox"

const FeedPhoto = (props, context) => {
    return (
        <div className={styles.feedPhoto}>
            <header className={styles.header}>
                <img 
                    className={styles.image}
                    src={ props.creator.profile_image || require("images/noPhoto.jpeg")}
                    alt={props.creator.username} 
                />
                <div className={styles.headerColumn}>
                    <span className={styles.creator}>{ props.creator.username }</span>
                    <span className={styles.location}>{ props.location }</span>
                </div>
            </header>
            <img src={props.file} alt={props.caption} />

            <div className={styles.meta}>
                <PhotoActions 
                    number = {props.like_count} 
                    isLiked={props.is_liked} 
                    photoId={props.id}
                />
                <PhotoComments 
                    caption = {props.caption}
                    creator = {props.creator.username}
                    comments = {props.comments}
                />
                <TimeStamp time={props.natural_time} />
                <CommentBox 
                    photoId={props.id}
                />
            </div>
        </div>
    )
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
    comments : PropTypes.arrayOf(
        PropTypes.shape({
            message : PropTypes.string.isRequired,
            creator : PropTypes.shape({
                profile_image: PropTypes.string,
                username: PropTypes.string.isRequired
            }).isRequired,
        })
    ).isRequired,
    natural_time : PropTypes.string.isRequired,
    is_liked : PropTypes.bool.isRequired
}

export default FeedPhoto;
