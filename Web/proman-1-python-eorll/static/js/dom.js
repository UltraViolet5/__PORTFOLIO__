// It uses data_handler.js to visualize elements
import {dataHandler} from "./data_handler.js";
import {element} from "./elements.js";
import * as events from "./events.js";

export let dom = {
    init: function () {
        // This function should run once, when the page is loaded.
        this.loadBoards();
        events.init();
    },

    showBoards: function (boards) {
        // shows boards appending them to #boards div
        let boardBox = $('#boards-container');
        for (let board of boards) {
            let newBoard = element.getBoard(board);
            boardBox.append(newBoard);
            dom.loadCards(`${board.id}`);
        }
    },
    loadBoards: function () {
        // retrieves boards and makes showBoards called
        dataHandler.getBoards(function (boards) {
            dom.showBoards(boards);
        });
    },
    loadCards: function (boardId) {
        dataHandler.getCardsByBoardId(boardId, function (cards) {
            dom.showStatuses(cards, boardId);
            dom.showCards(cards, boardId);
        });
    },
    showCards: function (cards, boardId) {
        for (let card of cards) {
            let cardBox = $(`#card-box-${card.status_id.split(" ").join("")}-${boardId}`);
            let newCard = element.getCard(card);
            cardBox.append(newCard);
        }
    },
    showStatuses: function (cards, boardId) {
        let cardsStatuses = [];
        let columnBox = $(`#board-${boardId} .card-body .container-fluid .project-col-container`);
        for (let card of cards) {
            if (!(cardsStatuses.includes(card.status_id))) {
                cardsStatuses.push(card.status_id);
            }
        }
        for (let status of cardsStatuses) {
            let newColumn = element.getColumn(status, boardId);
            columnBox.append(newColumn);
        }
    },
    loadBoard: function (board) {
        let newBoard = element.getBoard(board);
        newBoard.insertBefore($('#boards-container').children()[0]);
    },
    reloadBoards: function () {
        this.removeBoards();
        this.loadBoards();
    },
    removeBoards: function () {
        $('#boards-container').children().remove();
    }
};
