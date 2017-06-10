function draw() {
    var canvas = document.getElementById('rectangles');
    if (canvas.getContext) {
        var ctx = canvas.getContext('2d');
        return ctx;
    }
}

function init() {
    let ctx = draw();
    let rectanglesA = [];
    let rectanglesB = [];
    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 2; j++) {
            for (let k = i+1; k < 2+1; k++) {
                for (let l = j+1; l < 2+1; l++) {
                    let tlx = 50 + 100 * i;
                    let tly = 50 + 100 * j;
                    let brx = 50 + 100 * k;
                    let bry = 50 + 100 * l;
                    rectanglesA.push([tlx, tly, brx, bry]);
                }
            }
        }
    }
    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 2; j++) {
            for (let k = i+1; k < 2+1; k++) {
                for (let l = j+1; l < 2+1; l++) {
                    let tlx = 100 + 100 * i;
                    let tly = 100 + 100 * j;
                    let brx = 100 + 100 * k;
                    let bry = 100 + 100 * l;
                    rectanglesB.push([tlx, tly, brx, bry]);
                }
            }
        }
    }
    let indexA = 0;
    let indexB = 0;
    window.setInterval(
        () => {
            ctx.fillStyle = '#FFFFFF';
            ctx.fillRect(0, 0, 500, 500);
            drawDots(ctx);
            drawStrokeRectangle(ctx, rectanglesA[indexA]);
            drawStrokeRectangle(ctx, rectanglesB[indexB]);
            overlay = getOverlayingRectangle(rectanglesA[indexA], rectanglesB[indexB]);
            if (overlay !== null) {
                ctx.fillStyle = 'rgb(255, 0, 0)';
                drawFillRectangle(ctx, overlay);
            }
            indexB++;
            if (indexB === rectanglesB.length) {
                indexB = 0;
                indexA++;
            }
            if (indexA === rectanglesA.length) {
                indexA = 0;
            }
        },
        1000
    );
}

function drawStrokeRectangle(ctx, rectangle) {
    ctx.strokeStyle = 'rgb(0, 0, 0)';
    ctx.strokeRect(rectangle[0], rectangle[1], rectangle[2]-rectangle[0], rectangle[3]-rectangle[1]);
}

function drawFillRectangle(ctx, rectangle) {
    ctx.strokeStyle = 'rgb(0, 0, 0)';
    ctx.fillRect(rectangle[0], rectangle[1], rectangle[2]-rectangle[0], rectangle[3]-rectangle[1]);
}

function drawDots(ctx) {
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            for (let k = 0; k < 2; k++) {
                if (k === 0) 
                    ctx.fillStyle = 'rgb(200, 0, 0)';
                else
                    ctx.fillStyle = 'rgb(0, 200, 0)';
                ctx.beginPath();
                let x = 50 + 100 * i + 50 * k;
                let y = 50 + 100 * j + 50 * k;
                let radius = 5;
                let startAngle = 0;
                let endAngle = Math.PI * 2;
                ctx.arc(x, y, radius, startAngle, endAngle);
                ctx.fill();
            }
        }
    }
}

function getOverlayingRectangle(s1, s2) {
    so = [0, 0, 0, 0];
    
    if (s1[0] < s2[0])
        so[0] = s2[0];
    else
        so[0] = s1[0];

    if (s1[1] < s2[1])
        so[1] = s2[1];
    else
        so[1] = s1[1];

    if (s1[2] < s2[2])
        so[2] = s1[2];
    else
        so[2] = s2[2];

    if (s1[3] < s2[3])
        so[3] = s1[3];
    else
        so[3] = s2[3];

    if (so[0] < so[2] && so[1] < so[3])
        return so;
    else
        return null;
}

