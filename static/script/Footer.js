Vue.component('vue-footer-contacts', {
    template: `<div class="bottom_container">
        <ol>
            <p>Contacts:</p>
            <li>+7(708)909-90-17</li>
            <li>+7(708)909-90-17</li>
            <li>+7(708)909-90-17</li>
        </ol>
    </div>`
    });

    Vue.component('vue-footer-adress', {
        template: `<div class="bottom_container">
        <ul>
            <p>Adress:</p>
            <li>
                Al-Farabi str., 91 build., 3 floor.
            </li>
            <li>
                Kabanbay batyr str., 150 build., 2 floor.
            </li>
        </ul>
    </div>`
    });

    Vue.component('vue-footer-social', {
        template: `<div class="bottom_container">
        <i>Instagram: </i>
        <p>@instagram</p>
        <i>E-mail:</i>
        <p>mail@gmail.com</p>
    </div>`
    });

    Vue.component('vue-footer-news', {
        template: `<div class="bottom_container">
        <p>News letter: </p>
        <div style="display: flex;">
            <input type="text" name="subscribe" id="sub" style="margin-right: 5%;">
            <button class="btn btn-outline-light">Subscribe</button>
        </div>
    </div>`
    });
    
    new Vue({
        el: '#bottom_part'
    });