
class Video {
    constructor(title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }
    watch() {
        console.log(`${this.uploader} watched all ${this.time} minutes of ${this.title}!`);
    }
}




const video1 = new Video("Dark knight", "Ash", 120);
video1.watch();

const video2 = new Video("batman", "Sythe", 180);
video2.watch();

