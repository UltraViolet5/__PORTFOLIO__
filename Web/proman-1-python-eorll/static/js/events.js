import {element} from "./elements.js";
import * as domObj from "./dom.js";
import {dataHandler} from "./data_handler.js";

export function init() {
    initDraggingBoard();
    manualSync();
    initEventAddBoardBtn();
}

export function initEditingColumnName(obj$) {
    obj$.find('.project-status-title').on('dblclick', onDblClick);
}

export function initEditingBoardName(obj$) {
    obj$.find('.project-board-title').on('dblclick', onDblClick);
}

export function initAddColumnBtn(board$) {
    board$.find('.new-col').click(addColumn);
}

export function onDragCard(card$) {
    card$.get(0).addEventListener('dragstart', onDragStart);
    card$.get(0).addEventListener('dragend', onDragEnd);
    card$.get(0).addEventListener('drag', onDrag);

    card$.get(0).addEventListener('dragover', allowDrop);
    card$.get(0).addEventListener('drop', onDropBeforeCard);
}

export function onDropCardOverColumn(col$) {
    col$.get(0).addEventListener('drop', onDropInColumn);
    col$.get(0).addEventListener('dragover', allowDrop);
}

export function initDraggingColumns(board$) {
    board$.find(".project-col-container").sortable({
        tolerance: "pointer",
        opacity: 0.5,
        placeholder: "placeholder",
        start: function (e, ui) {
            ui.placeholder.height(ui.item.height());
            ui.placeholder.width(ui.item.width());
            $(ui.placeholder).hide(300);
        },
        change: function (e, ui) {
            $(ui.placeholder).hide().show(300);
        }
    });
}

export function initDraggingBoard() {
    $("#boards-container").sortable({
        start: function (e, ui) {
            ui.placeholder.height(ui.item.height());
            ui.placeholder.width(ui.item.width());
            $(ui.placeholder).hide(300);
        },
        change: function (e, ui) {
            $(ui.placeholder).hide().show(300);
        }
    });
}

export function initRemoveParent(obj$) {
    obj$.find(".delete-parent").click(removeParent);
}

export function initHideColumns(board$) {
    board$.find(".hide-col").click(hideColumns);
}

function onDblClick(e) {

    let input = $('<input>');
    input.attr('type', 'text');

    if ($(e.target).hasClass('project-status-title')) {
        input.addClass('input d-inline-block bg-transparent text-light border-0 my-0 text-center w-100');
    } else if ($(e.target).hasClass('project-board-title')) {
        input.addClass('input d-inline-block bg-transparent text-light border-0 my-0');
    }

    input.val(e.target.innerText);

    $(e.target).addClass('d-none');
    $(e.target).after(input);
    input.focus();
    input.select();

    input.on('keypress', function (e) {
        // If you pressed enter
        if (e.which === 13) {
            renameBoardNode($(e.target));
        }
    });
    input.on('focusout', function (e) {
        renameBoardNode($(e.target));
    });
    $(document).on('keydown', function (e) {
        if (e.which === 27) {
            displayTitle($(e.target));
        }
    });
}

function renameBoardNode(input$) {
    let newTitle = input$.val();
    input$.prev().text(newTitle);
    displayTitle(input$);
}

function displayTitle(input$) {
    input$.prev().removeClass('d-none');
    input$.remove();
}


function addColumn(e) {
    let columnsContainer = $(this).parent().parent().next();

    let newColumn = element.getColumn('New column', columnsContainer.parent('.project-boards').attr('id'));

    let input = $("<input>", {
        type: "text",
        class: "input title-input w-100 text-center",
        id: "inputCont",
        value: "New column"
    });
    applyCancelAddingCol(input, newColumn);

    newColumn.find('.project-status-title').addClass('d-none');
    newColumn.find('.project-status-title').after(input);

    columnsContainer.prepend(newColumn);
    input.select();
    input.focus();

}

function allowDrop(e) {
    e.preventDefault();
}

function onDragStart(e) {
    console.log('Drag start.');
    e.currentTarget.classList.add('dragging');
    e.dataTransfer.setData("text", e.currentTarget.id);
}

function onDrag(e) {
}


function onDragEnd(e) {
    console.log('Drag end.');
    e.currentTarget.classList.remove('dragging');
}

function onDropInColumn(e) {
    console.log('Drop in column.');

    let id = e.dataTransfer.getData("text");
    let draggedElement = $(`#${id}`);
    let previousParent = draggedElement.parent();

    $(e.currentTarget).find('.card-container').append(draggedElement);
    _updateCardsorders($(e.currentTarget).find('.card-container').children());
    _updateCardsorders(previousParent.children());
}

function onDropBeforeCard(e) {
    e.stopPropagation();
    console.log('Drop before card.');

    let id = e.dataTransfer.getData("text");
    let draggedElement = $(`#${id}`);
    let previousParent = draggedElement.parent();

    $(e.currentTarget).before(draggedElement);

    _updateCardsorders($(e.currentTarget).parent().children());
    _updateCardsorders(previousParent.children());
}


export function initAddCardBtnEvent(column$) {
    let addBtn = column$.find('.project-add-card');
    addBtn.on("click", function (e) {
        let card = {'id': -1, 'title': 'New card', 'order': -1};
        let button = element.getCard(card);
        button.children().addClass('d-none');

        let input = $('<input type="text" class="input d-inline-block w-100 border-light text-center" placeholder="New task" value="New task">');

        button.find('h6').after(input);
        $(e.currentTarget).prev().append(button);
        applyCancelAddingCard(button, input);

        input.select();
        input.focus();
    });
}

export function renameCard(e) {
    $(e.currentTarget).children().addClass('d-none');
    let input = $('<input type="text" class="input d-inline-block w-100 border-light text-center"' +
        ` placeholder="New task" value="${$(e.currentTarget).find('h6').text()}">`);
    applyCancelRenaming($(e.currentTarget), input)
    $(e.currentTarget).find('h6').after(input);
    input.select();
    input.focus();
}

function applyCancelRenaming(card, input) {
    applyCardName(card, input)
    $(document).on('keydown', function (e) {
        if (e.which === 27) {
            card.find('input').remove();
            card.children().removeClass('d-none');
            card.find('h1').text('New task');
        }
    });
}

function applyCancelAddingCard(card, input) {
    applyCardName(card, input)
    $(document).on('keydown', function (e) {
        // If you pressed esc
        if (e.which === 27) {
            card.find('input').parent().remove();
        }
    });
}

function applyCardName(card, input) {
    input.on('keypress', function (e) {
        // If you pressed enter
        if (e.which === 13) {
            _applyCardName(card);
        }
    });
    input.on('focusout', function (e) {
        // If click to another node
        _applyCardName(card);
    });
}

function applyCancelAddingCol(input, column) {
    $(document).on('keydown', function (e) {
        if (e.which === 27) {
            column.remove();
        }
    });
    input.on('keypress', function (e) {
        // If you pressed enter
        if (e.which === 13) {
            console.log(column.find('.project-status-title'));
            column.find('.project-status-title').text(input.val())
            column.find('.project-status-title').removeClass('d-none');
            input.remove();
            $(document).off('keydown');
        }
    });
    input.on('focusout', function (e) {
        column.find('.project-status-title').text(input.val())
        column.find('.project-status-title').removeClass('d-none');
        input.remove();
        $(document).off('keydown');
    });
}

function removeParent(e) {
    $(e.target).parent().remove()
}


function hideColumns(e) {
    let cardBody = $(e.target).parent().siblings(".card-body")
    cardBody.toggle(500)
}

function _updateCardsorders(cards$) {
    cards$.each(function (i) {
        $(this).attr('data-order', i);
        $(this).find('.badge').text(i);
    });
}

function _applyCardName(card$) {
    card$.children().removeClass('d-none');
    card$.find('h6').text(card$.find('input').val());
    card$.find('input').remove();
    $(document).off('keydown');
    _updateCardsorders(card$.parent().children());
}

function manualSync() {
    $('#manual-sync').on('click', function () {
         domObj.dom.reloadBoards();
    });
}

export function initEventAddBoardBtn() {
        let btn = document.getElementById('add-board-btn');
        btn.addEventListener('click', event => {
            let boardForm = new FormData(document.getElementById('new-board-form'));
            dataHandler.createNewBoard(boardForm, function (board) {
                domObj.dom.loadBoard(board);
            });
            $(`#addBoard`).modal('hide');
        })
    }
