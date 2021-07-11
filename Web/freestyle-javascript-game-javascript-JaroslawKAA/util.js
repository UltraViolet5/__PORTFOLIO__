export function rndBetween(min, max) {
    return Math.floor(
        Math.random() * (max - min + 1) + min
    )
}

let startTime;
export let elapsedTime = 0;
let timerInterval;
let firstClick = true;

function stopWatchStart()
    {
    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(function printTime() {
        elapsedTime = Date.now() - startTime;
        print(timeToString(elapsedTime));
    }, 10);

}

function print(txt) {
  document.getElementById("stopwatch").innerHTML = txt;
}

export function timeToString(time) {
  let diffInHrs = time / 3600000;
  let hh = Math.floor(diffInHrs);

  let diffInMin = (diffInHrs - hh) * 60;
  let mm = Math.floor(diffInMin);

  let diffInSec = (diffInMin - mm) * 60;
  let ss = Math.floor(diffInSec);

  let diffInMs = (diffInSec - ss) * 100;
  let ms = Math.floor(diffInMs);

  let formattedMM = mm.toString().padStart(2, "0");
  let formattedSS = ss.toString().padStart(2, "0");
  let formattedMS = ms.toString().padStart(2, "0");

  return `${formattedMM}:${formattedSS}:${formattedMS}`;
}

export function clickFirstTime()
{
    if (firstClick)
    {
        stopWatchStart()
        firstClick = false
    }
}

    export function pause() {
    console.log("pause");
    clearInterval(timerInterval);

}