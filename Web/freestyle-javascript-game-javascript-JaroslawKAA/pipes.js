import {orientation} from "./enums.js";

export class Pipe {
    constructor(x = 0,
                y = 0,
                water = false,
                draggable = true,
                id = null,
                orientation = 1) {
        this.x = x;
        this.y = y;
        this.water = water;
        this.draggable = draggable;
        this.id = id;
        this.orientation = orientation;
    }

    name = 'defaultName';
    img = '/';
    imgWater = '/';
    holes = [];

    rotateLeft() {
        let node = this.getNode();
        if (node.classList.contains('up')) {
            node.classList.remove("up");
            node.classList.add("left");
        } else if (node.classList.contains('left')) {
            node.classList.remove("left");
            node.classList.add("down");
        } else if (node.classList.contains('down')) {
            node.classList.remove("down");
            node.classList.add("right");
        } else if (node.classList.contains('right')) {
            node.classList.remove("right");
            node.classList.add("up");
        }
        this.orientation--;
        if (this.orientation < orientation.up) {
            this.orientation = orientation.left;
        }
        this.rotateHolesLeft();
        this.rotateHoleClassesLeft(node);
    }

    rotateRight() {
        let node = this.getNode();
        if (this.orientation === orientation.up) {
            node.classList.remove("up");
            node.classList.add("right");
        } else if (this.orientation === orientation.left) {
            node.classList.remove("left");
            node.classList.add("up");
        } else if (this.orientation === orientation.down) {
            node.classList.remove("down");
            node.classList.add("left");
        } else if (this.orientation === orientation.right) {
            node.classList.remove("right");
            node.classList.add("down");
        }
        this.orientation++;
        if (this.orientation > orientation.left) {
            this.orientation = orientation.up;
        }
        this.rotateHolesRight();
    }

    _setOrientation(orientation) {
        let difference = Math.abs(this.orientation - orientation);
        for (let i = 0; i < difference; i++) {
            this._rotateRight();
            this.rotateHolesRight();
        }
    }

    _rotateRight() {
        this.orientation++;
        if (this.orientation > orientation.left) {
            this.orientation = orientation.up;
        }
    }

    rotateHolesLeft() {
        let i = 0;
        for (let hole of this.holes) {
            this.holes[i]--;
            if (this.holes[i] < orientation.up) {
                this.holes[i] = orientation.left;
            }
        }
    }

    rotateHoleClassesLeft(node) {
        let classes = [];
        node.classList.forEach((c) => classes.push(c));
        for (let i = 0; i < classes.length; i++) {
            if (classes[i] === 'hole-up') {
                classes[i] = 'hole-left';
            } else if (classes[i] === 'hole-left') {
                classes[i] = 'hole-down';
            } else if (classes[i] === 'hole-down') {
                classes[i] = 'hole-right';
            } else if (classes[i] === 'hole-right') {
                classes[i] = 'hole-up';
            }
        }
        node.className = classes.join(' ');
    }

    rotateHolesRight() {
        let i = 0;
        for (let hole of this.holes) {
            this.holes[i]++;
            if (this.holes[i] > orientation.left) {
                this.holes[i] = orientation.up;
            }
            i++;
        }
    }

    fillPipe() {
        this.water = true;
    }

    emptyPipe() {
        this.water = false;
    }

    getNode() {
        return document.querySelector('[data-col="${}"]'.replace('${}', this.x.toString()) +
            '[data-row="${}"]'.replace('${}', this.y.toString()));
    }

    rewriteNodeClasses(classes) {
        let node = this.getNode();
        node.classList.remove(...node.classList);
        node.classList.add(...classes);
    }
}

export class PipeStraight
    extends Pipe {
    constructor(x = 0,
                y = 0,
                water = false,
                draggable = true,
                id = null,
                orientation = 1) {
        super(x, y, water, draggable, id, orientation);
    }

    name = 'pipeStraight';
    img = '/img/rura-prosta.png';
    imgWater = '/img/rura-ptosta-woda.png';
    holes = [orientation.left, orientation.right];
}

export class PipeStraightEnd extends Pipe {
    constructor(x = 0, y = 0, water = false, draggable = false, id = null, orientation = 1) {
        super(x, y, water, draggable, id, orientation);
    }

    name = 'end';
    img = '/img/rura-prosta-koniec.png';
    imgWater = '/img/rura-prosta-koniec.png';
}


export class PipeThree extends Pipe {
    constructor(x = 0,
                y = 0,
                water = false,
                draggable = true,
                id = null,
                orientation = 1) {
        super(x, y, water, draggable, id, orientation);
    }

    name = 'pipeThree';
    img = '/img/rura-3.png';
    imgWater = '/img/rura-3-WODA.png';
    holes = [orientation.left, orientation.up, orientation.right];
}

export class PipeFolded extends Pipe {
    constructor(x = 0,
                y = 0,
                water = false,
                draggable = true,
                id = null,
                orientation = 1) {
        super(x, y, water, draggable, id, orientation);
    }

    name = 'pipeFolded';
    img = '/img/rura-skretna.png';
    imgWater = '/img/rura-skret-woda.png';
    holes = [orientation.left, orientation.down];
}

export class EmptyField extends Pipe {
    constructor(x = 0, y = 0, draggable = true, id = null) {
        super(x, y, false, draggable, id);
    }

    name = 'empty';
    img = '/img/rura-pusty.png';
}