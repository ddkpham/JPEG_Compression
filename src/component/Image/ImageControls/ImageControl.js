import React, { Component } from 'react';

import classes from './ImageControl.module.css';
import Image from '../Image'

class ImageControl extends Component{
    render(){
        let images = this.props.images.map((image)=>[
             <Image 
             imagePath={image.filePath} 
             key={image.id}/>
        ]);
        console.log(images)
        return(
            <div className={classes.ImageControl}>
                {images}
            </div>
        )
    }
} 



export default ImageControl;