import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.module.scss";
import Loading from "components/Loading"

const Feed = props => {
    if(props.loading){
        return <LoadingFeed />
    }else{
        return <RenderFeed {...props}/>
    }
}

const LoadingFeed = props => (
    <div className={styles.feed} >
        <Loading />
    </div>
);

const RenderFeed = props => (
    <div className={styles.feed}>{props.feed.map(post => post.caption)}</div>
)

Feed.propTypes = {
    loading : PropTypes.bool.isRequired
};

export default Feed;