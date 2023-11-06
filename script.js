const main = document.querySelector('main');

function headingFactory(color){
    function createHeading(text){
        const heading = document.createElement('h1');
        heading.setAttribute('style', 'color: ' + color);
        heading.textContent = text;
        return heading;
    }
return createHeading;
}

const red = headingFactory("red");
const blue = headingFactory("blue")

const factory1 = red("using factory 1") 
const factory2 = blue("using factory 2") 

main.appendChild(factory1);
main.appendChild(factory2);

