export default class Playground {
    constructor(width = 5, height = 5) {
        this.width = width;
        this.height = height;
        // water start can be only on down edge
        this.waterStart = {'x': 0, 'y': height - 1};
        // water edn can be only on right edge
        this.waterEnd = {'x': width-1, 'y': 0};
        this.size = this.height * this.width;
    }
}
