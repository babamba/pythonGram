import React from "react";
import PropTypes from "prop-types"
import Textarea from "react-textarea-autosize";
import styles from "./styles.module.scss"

const CommentBox = (props, context) => (
        <form className={styles.commentBox}>
            <Textarea placeholder={context.t("Add a Comment...")} className={styles.input} ></Textarea>
        </form>
)

CommentBox.contextTypes = {
    t: PropTypes.func.isRequired
}

CommentBox.propTypes = {

}

export default CommentBox;
