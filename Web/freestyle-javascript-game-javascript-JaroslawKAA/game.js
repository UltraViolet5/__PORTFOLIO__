import {EmptyField, PipeFolded, PipeStraight, PipeStraightEnd, PipeThree} from "./pipes.js";
import * as playgrounds from "./playgrounds.js";
import {rndBetween, clickFirstTime, pause, elapsedTime, timeToString} from "./util.js";
import {orientation} from "./enums.js";

const game = {

    init: function () {
        // Your game can start here, but define separate functions, don't write everything in here :)
        this.drawBoard(pipes);
        this.initClick();
        this.resetButtonClick();
        this.checkWaterPath();
        game.createScoreBoard(game.numberOfWins());
    },

    drawBoard(pipes) {
        let gameZoneDiV = document.querySelector(".game_board");

        for (let i = 0; i < playgrounds.firstPlayground.height; i++) {
            let gameRow = document.createElement("div");

            gameRow.classList.add("gameRow");
            gameZoneDiV.appendChild(gameRow);
            for (let j = 0; j < playgrounds.firstPlayground.width; j++) {
                let field = document.createElement("div");

                this.setPipeTypeClass(pipes, field, i, j);
                this.setOrientationClass(pipes, field, i, j);
                field.setAttribute('data-row', i.toString());
                field.setAttribute('data-col', j.toString());

                if (pipes[i][j].water) {
                    field.classList.add("water");
                }
                if (pipes[i][j].draggable) {
                    field.draggable = true;
                }
                gameRow.appendChild(field);
            }
        }
        this.addIdToPipeNodes(pipes);
        this.setHoleClasses();
    },
    initPipes(playground) {
        let pipes = [];
        let index = 0;
        for (let i = 0; i < playground.height; i++) {
            pipes.push([]);
            for (let j = 0; j < playground.width; j++) {
                if (i !== playground.height - 1 && j !== playground.width - 1) {
                    // standard pipes
                    pipes[i].push(this.getRandomPipe(j, i, index));
                    index++;
                } else {
                    // interface pipes
                    if (j === playground.waterStart['x']
                        && i === playground.waterStart['y']) {
                        // Start pipe
                        pipes[i].push(new PipeThree(j, i, true, false, index))
                        index++;
                    } else if (i === playground.height - 1) {
                        // Down straight pipes
                        pipes[i].push(new PipeStraight(j, i, true, false, index));
                        index++;
                    } else if (j === playground.waterEnd['x'] &&
                        i === playground.waterEnd['y']) {
                        // End pipe
                        pipes[i].push(new PipeStraightEnd(j, i, false, false, index));
                        index++;
                    } else if (j === playground.width - 1 &&
                        i !== playground.waterEnd['y'] &&
                        i !== playground.height - 1) {
                        // Empty fields
                        pipes[i].push(new EmptyField(j, i, false, index))
                        index++;
                    }
                }
            }
        }
        return pipes;
    },
    getRandomPipe(x, y, id) {
        let rndType = rndBetween(0, 2);
        let rndRotation = rndBetween(1, 4);
        switch (rndType) {
            case 0:

                let pipe1 = new PipeStraight(x, y, false, true, id);
                pipe1._setOrientation(rndRotation);
                return pipe1;
            case 1:

                let pipe2 = new PipeFolded(x, y, false, true, id);
                pipe2._setOrientation(rndRotation);
                return pipe2;
            case 2:

                let pipe3 = new PipeThree(x, y, false, true, id);
                pipe3._setOrientation(rndRotation);
                return pipe3;
            default:
                throw 'Wrong random number in switch statement.';
        }
    },
    setOrientationClass(pipes, field, i, j) {
        //    add to all nodes orientation class

        switch (pipes[i][j].orientation) {
            case orientation.up:
                field.classList.add('up');
                break;
            case orientation.right:
                field.classList.add('right');
                break;
            case orientation.down:
                field.classList.add('down');
                break;
            case orientation.left:
                field.classList.add('left')
        }
    },
    setPipeTypeClass(pipes, field, i, j) {
        //    add to all nodes specific pipe class
        if (pipes[i][j].name === 'pipeStraight') {
            field.classList.add("PipeStraight");
        } else if (pipes[i][j].name === 'pipeFolded') {
            field.classList.add("PipeFolded");
        } else if (pipes[i][j].name === 'pipeThree') {
            field.classList.add("PipeThree");
        } else if (pipes[i][j].name === 'empty') {
            field.classList.add("empty");
        } else if (pipes[i][j].name === 'end') {
            field.classList.add("PipeStraightEnd");

        }
    },
    setHoleClasses() {
        //    add to all nodes specific hole class
        for (let i = 0; i < playgrounds.firstPlayground.height; i++) {
            for (let j = 0; j < playgrounds.firstPlayground.width; j++) {
                for (let hole of pipes[i][j].holes) {
                    let field = this.getField(j, i);
                    switch (hole) {
                        case orientation.up:
                            field.classList.add('hole-up');
                            break;
                        case orientation.right:
                            field.classList.add('hole-right');
                            break;
                        case orientation.down:
                            field.classList.add('hole-down');
                            break;
                        case orientation.left:
                            field.classList.add('hole-left');
                    }
                }
            }
        }
    },

    // Events ------------------------------------------------------
    initClick() {
        let pipesNode = document.querySelectorAll(
            '.PipeStraight, .PipeFolded, .PipeThree');

        for (let pipe of pipesNode) {
            if (pipe.draggable === true) {
                pipe.addEventListener("click", this.onClick.bind(this));
                pipe.addEventListener("dragstart", this.onDragStart.bind(this));
                pipe.addEventListener("drop", this.onDrop.bind(this));
                pipe.addEventListener("dragover", this.onDragOver.bind(this));
                pipe.addEventListener("dragover", this.allowDrop);
                pipe.addEventListener("dragleave", this.onDragLeave.bind(this));
                pipe.addEventListener("dragend", this.onDragEnd);
                pipe.addEventListener("click", clickFirstTime);
                pipe.addEventListener("dragstart", clickFirstTime);
                // pipe.addEventListener("click", this.winCondition);
                // pipe.addEventListener("drop", this.winCondition);


            }
        }
    },
    onClick(e) {
        this.rotateLeftEvent(e);
        this.checkWaterPath();
        this.winCondition()
    },
    rotateLeftEvent: function (e) {
        let pipe = this.getPipeByEvent(e);
        pipe.rotateLeft();
    },
    onDragStart(e) {
        console.log("Drag Start");
        e.dataTransfer.setData('text', e.target.id);
        console.log(e.target);
        e.target.classList.add('draggedElement');
    },
    allowDrop(e) {
        e.preventDefault();
    },
    onDrop(e) {
        e.preventDefault();
        console.log('Drop');
        let draggedPipeId = parseInt(e.dataTransfer.getData('text'));
        let replacedPipeId = parseInt(e.target.getAttribute('id'));
        this.swapPines(draggedPipeId, replacedPipeId);
        this.checkWaterPath();
        this.getFieldById(draggedPipeId).classList.remove('ifOverElement');
        this.getFieldById(draggedPipeId).classList.remove('draggedElement');
        e.currentTarget.classList.remove('draggedElement');
        e.currentTarget.classList.remove('ifOverElement');
        e.dataTransfer.clearData();
        this.winCondition()
    },
    onDragOver(e) {
        e.currentTarget.classList.add('ifOverElement');
    },
    onDragLeave(e) {
        e.currentTarget.classList.remove('ifOverElement');
    },

    onDragEnd(e) {
        console.log('Drag End');
        e.target.classList.remove('draggedElement');
    },

    resetButtonClick() {
        let button = document.querySelector(".button_reset")
        button.addEventListener("click", this.onResetButtonClick)
    },

    onResetButtonClick() {
        window.location.reload();
    },

    // END Events ================================================================

    checkWaterPath() {
        let xStart = playgrounds.firstPlayground.waterStart['x'];
        let yStart = playgrounds.firstPlayground.waterStart['y'];

        let startPipe = this.getField(xStart, yStart);
        this.removeWaterClassFromNodes();
        this.fillWaterAround(startPipe);

    },
    fillWaterAround(pipeNode) {
        const pipeX = parseInt(pipeNode.getAttribute('data-col'));
        const pipeY = parseInt(pipeNode.getAttribute('data-row'));
        if (pipeNode.classList.contains('hole-up')) {
            let up_node = this.getField(pipeX, pipeY - 1);
            if (up_node !== null && up_node.classList.contains('hole-down') &&
                !up_node.classList.contains('water')) {
                up_node.classList.add('water');
                this.fillWaterAround(up_node);
            }
        }
        if (pipeNode.classList.contains('hole-right')) {
            let right_node = this.getField(pipeX + 1, pipeY);
            if (right_node !== null && right_node.classList.contains('hole-left') &&
                !right_node.classList.contains('water')) {
                right_node.classList.add('water');
                this.fillWaterAround(right_node);
            }
        }
        if (pipeNode.classList.contains('hole-down')) {
            let down_node = this.getField(pipeX, pipeY + 1);
            if (down_node !== null && down_node.classList.contains('hole-up') &&
                !down_node.classList.contains('water')) {
                down_node.classList.add('water');
                this.fillWaterAround(down_node);
            }
        }
        if (pipeNode.classList.contains('hole-left')) {
            let left_node = this.getField(pipeX - 1, pipeY);
            if (left_node !== null && left_node.classList.contains('hole-right') &&
                !left_node.classList.contains('water')) {
                left_node.classList.add('water');
                this.fillWaterAround(left_node)
            }
        }
    },
    removeWaterClassFromNodes() {
        let nodes = document.querySelectorAll('[draggable = "true"]');
        for (let node of nodes) {
            node.classList.remove('water');
        }
    },
    addIdToPipeNodes(pipes) {
        let i = 0;
        for (let row of pipes) {
            let j = 0;
            for (let pipe of row) {
                let pipeNode = pipe.getNode();
                pipeNode.setAttribute('id', pipe.id);
                j++;
            }
            i++;
        }
    },
    getField(x, y) {
        return document.querySelector('[data-col="${}"]'.replace('${}', x) +
            '[data-row="${}"]'.replace('${}', y));
    },
    getFieldById(id) {
        return document.querySelector('[id="${}"]'.replace('${}', id.toString()));
    },
    getPipeByEvent(event) {
        let pipeNode = event.target;
        let pipeId = pipeNode.getAttribute('id');
        return this.getPipeById(parseInt(pipeId));
    },
    getPipeById(id) {
        for (let row of pipes) {
            for (let pipe of row) {
                if (pipe.id === id) {
                    return pipe;
                }
            }
        }
    },
    getPipeIndexes(id) {
        let i = 0;
        for (let row of pipes) {
            let j = 0;
            for (let pipe of row) {
                if (pipe.id === id) {
                    return {'x': j, 'y': i}
                }
                j++;
            }
            i++;
        }
    },
    swapPines(id1, id2) {
        // swap two pipes places
        let firstPipeIndexes = this.getPipeIndexes(id1);
        let secondPipeIndexes = this.getPipeIndexes(id2);
        const temp = pipes[firstPipeIndexes['y']][firstPipeIndexes['x']];
        pipes[firstPipeIndexes['y']][firstPipeIndexes['x']] = pipes[secondPipeIndexes['y']][secondPipeIndexes['x']];
        pipes[secondPipeIndexes['y']][secondPipeIndexes['x']] = temp;
        this.swapPipesNodeClasses(id1, id2);
    },
    swapPipesNodeClasses(id1, id2) {
        let firstClasses = document.getElementById((id1).toString()).className;
        let secondClasses = document.getElementById((id2).toString()).className;
        document.getElementById(id1.toString()).className = secondClasses;
        document.getElementById(id2.toString()).className = firstClasses;
    },
    winCondition() {
        let endPipe = document.getElementById("4");
        if (endPipe.classList.contains("water") && endPipe.classList.contains("hole-right")) {
            console.log("win");
            alert("YOU WON!");
            pause();

            let num = game.numberOfWins();

            console.log(num);
            game.addToStorage(num);
            // game.clearScoreBard();
            // game.createScoreBoard(num);

        }

    },
    clearScoreBard()
    {
        if (myStorage.length > 5)
        {
            let part =myStorage.length ;
            let partWithOutFiveScores = part -5;
            let parentNode = document.querySelector("ol")
            for(let i = partWithOutFiveScores; i >=0 ;i--)
            {
                parentNode.removeChild(parentNode.lastChild)
            }

        }
    },
    addToStorage(number)
    {
        number++;
        myStorage.setItem(`Time${number}`, timeToString(elapsedTime));
    },

    createScoreBoard(number)
    {
        let numberOf = Number(number)
        numberOf++
        if(numberOf !== 0) {
            let i= 1;
            let element = document.querySelector(".Score_Board_body")
            for (i ; i < numberOf; i++) {
                let Time = myStorage.getItem(`Time${i}`);
                let row = document.createElement('li');
                row.innerText = Time;
                element.prepend(row);

            }

        }
        game.clearScoreBard();
        game.setClassToTrs()
    },

    setClassToTrs()
    {
          let trs = document.querySelectorAll("li")
        for (let tr of trs){
            tr.classList.add("Score")

        }
    },

    numberOfWins() {


        return myStorage.length
    }

}

let myStorage = localStorage;
const pipes = game.initPipes(playgrounds.firstPlayground);
game.init();
