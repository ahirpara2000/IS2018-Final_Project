function sendReq(song_name, artist_name, song_image, song_audio, artist_list)
{
    const url = '/lyrics/' + song_name + '/' + artist_name;
    window.fetch(url).then(response => response.json())
        .then(data => {

            let lyrics_box = document.getElementById("lyrics_box");

            let text = document.getElementById("text");
            if(data['Lyrics'] === "Opps no lyrics found..!!")
            {
                text.style.color = 'red';
                text.style.textAlign = 'center';

                text.innerHTML = data['Lyrics'];
            }
            else
            {
                text.style.color = 'white';
                text.style.textAlign = 'left';

                var str = "Link to original lyrics page...";
                var lyrics_url = str.link(data['Lyrics'][0]);

                text.innerHTML = data['Lyrics'][1];
                text.innerHTML += lyrics_url;
            }

            let songImage = document.getElementById("image_box");
            songImage.src = song_image;

            let songName = document.getElementById("song_box");
            songName.innerHTML = song_name;


            let artist_box = document.getElementById("artist_box");
            artist_box.innerHTML = artist_list;

            let audioControl = document.getElementById('control');
            let songAudio = document.getElementById("audio_box");
            songAudio.src =  song_audio;
            songAudio.type = 'audio/ogg';
            audioControl.load();

            hideLoader();

            let background = document.getElementById("lyrics_bg");
            background.style.filter = "blur(5px)";

            lyrics_box.style.display = 'grid';
        });

}

function showLoader()
{
    var loader = document.getElementById("loader");
    loader.style.display = "block";
    let background = document.getElementById("lyrics_bg");
    background.style.filter = "blur(5px)";
}
function hideLoader()
{
    var loader = document.getElementById("loader");
    loader.style.display = "none";
    let background = document.getElementById("lyrics_bg");
    background.style.filter = 'none';
}
function checkAddon()
{
    let err = document.getElementById('goog-gt-tt');
    if(typeof(err) != 'undefined' && err != null)
    {
        var err_msg = document.getElementById("err_box");
        err_msg.style.display = "block";
        return true;
    }
    return false;
}

function alertUser()
{
    let err = document.getElementById('goog-gt-tt');
    if(typeof(err) != 'undefined' && err != null)
    {
        alert("It looks like you are using grammarly add-on.\nShow lyrics feature may not work while grammarly is active.");
    }
}

let selected_tab;
let song_name;
let artist_name;
let song_image;
let song_audio;
let artist_list;

window.onload = () => {
    alertUser();
    let tab = document.getElementById('tabf0');
    if(typeof(tab) != 'undefined' && tab != null)
    {
        tab.addEventListener('click', () => {

            if(!checkAddon())
            {
                song_name = document.getElementById("name0").innerHTML;
                artist_name = document.getElementById("artist_name").innerHTML;
                song_image = document.getElementById("image0").src;
                song_audio = document.getElementById("audio0").src;
                artist_list = document.getElementById("name_list0").innerHTML;
                selected_tab = 0;
                showLoader();
                sendReq(song_name, artist_name, song_image, song_audio, artist_list);
            }
        });
    }

    tab = document.getElementById('tabf1');
    if(typeof(tab) != 'undefined' && tab != null)
    {
        tab.addEventListener('click', () => {

            if(!checkAddon())
            {
                song_name = document.getElementById("name1").innerHTML;
                artist_name = document.getElementById("artist_name").innerHTML;
                ong_image = document.getElementById("image1").src;
                song_audio = document.getElementById("audio1").src;
                artist_list = document.getElementById("name_list1").innerHTML;
                selected_tab = 1;
                showLoader();
                sendReq(song_name, artist_name, song_image, song_audio, artist_list);
            }

        });
    }

    tab = document.getElementById('tabf2');
    if(typeof(tab) != 'undefined' && tab != null)
    {
        tab.addEventListener('click', () => {

            if(!checkAddon())
            {
                song_name = document.getElementById("name2").innerHTML;
                artist_name = document.getElementById("artist_name").innerHTML;
                song_image = document.getElementById("image2").src;
                song_audio = document.getElementById("audio2").src;
                artist_list = document.getElementById("name_list2").innerHTML;
                selected_tab = 2;
                showLoader();
                sendReq(song_name, artist_name, song_image, song_audio, artist_list);
            }

        });
    }

    tab = document.getElementById('tabf3');
    if(typeof(tab) != 'undefined' && tab != null)
    {
        tab.addEventListener('click', () => {

            if(!checkAddon())
            {
                song_name = document.getElementById("name3").innerHTML;
                artist_name = document.getElementById("artist_name").innerHTML;
                song_image = document.getElementById("image3").src;
                song_audio = document.getElementById("audio3").src;
                artist_list = document.getElementById("name_list3").innerHTML;
                selected_tab = 4;
                showLoader();
                sendReq(song_name, artist_name, song_image, song_audio, artist_list);
            }

        });
    }

    tab = document.getElementById('tabf4');
    if(typeof(tab) != 'undefined' && tab != null)
    {
        tab.addEventListener('click', () => {
            if(!checkAddon())
            {
                song_name = document.getElementById("name4").innerHTML;
                artist_name = document.getElementById("artist_name").innerHTML;
                song_image = document.getElementById("image4").src;
                song_audio = document.getElementById("audio4").src;
                artist_list = document.getElementById("name_list4").innerHTML;
                selected_tab = 4;
                showLoader();
                sendReq(song_name, artist_name, song_image, song_audio, artist_list);
            }

        });
    }
    tab = document.getElementById('tabf5');
    if(typeof(tab) != 'undefined' && tab != null)
    {
        tab.addEventListener('click', () => {

            if(!checkAddon())
            {
                song_name = document.getElementById("name5").innerHTML;
                artist_name = document.getElementById("artist_name").innerHTML;
                song_image = document.getElementById("image5").src;
                song_audio = document.getElementById("audio5").src;
                artist_list = document.getElementById("name_list5").innerHTML;
                selected_tab = 5;
                showLoader();
                sendReq(song_name, artist_name, song_image, song_audio, artist_list);
            }

        });
    }

    tab = document.getElementById('tabf6');
    if(typeof(tab) != 'undefined' && tab != null)
    {
        tab.addEventListener('click', () => {

            if(!checkAddon())
            {
                song_name = document.getElementById("name6").innerHTML;
                artist_name = document.getElementById("artist_name").innerHTML;
                song_image = document.getElementById("image6").src;
                song_audio = document.getElementById("audio6").src;
                artist_list = document.getElementById("name_list6").innerHTML;
                selected_tab = 6;
                showLoader();
                sendReq(song_name, artist_name, song_image, song_audio, artist_list);
            }

        });
    }

    tab = document.getElementById('tabf7');
    if(typeof(tab) != 'undefined' && tab != null)
    {
        tab.addEventListener('click', () => {

            if(!checkAddon())
            {
                song_name = document.getElementById("name7").innerHTML;
                artist_name = document.getElementById("artist_name").innerHTML;
                song_image = document.getElementById("image7").src;
                song_audio = document.getElementById("audio7").src;
                artist_list = document.getElementById("name_list7").innerHTML;
                selected_tab = 7;
                showLoader();
                sendReq(song_name, artist_name, song_image, song_audio, artist_list);
            }

        });
    }

    tab = document.getElementById('tabf8');
    if(typeof(tab) != 'undefined' && tab != null)
    {
        tab.addEventListener('click', () => {

            if(!checkAddon())
            {
                song_name = document.getElementById("name8").innerHTML;
                artist_name = document.getElementById("artist_name").innerHTML;
                song_image = document.getElementById("image8").src;
                song_audio = document.getElementById("audio8").src;
                artist_list = document.getElementById("name_list8").innerHTML;
                selected_tab = 8;
                showLoader();
                sendReq(song_name, artist_name, song_image, song_audio, artist_list);
            }

        });
    }


    tab = document.getElementById('tabf9');
    if(typeof(tab) != 'undefined' && tab != null)
    {
        tab.addEventListener('click', () => {

            if(!checkAddon())
            {
                song_name = document.getElementById("name9").innerHTML;
                artist_name = document.getElementById("artist_name").innerHTML;
                song_image = document.getElementById("image9").src;
                song_audio = document.getElementById("audio9").src;
                artist_list = document.getElementById("name_list9").innerHTML;
                selected_tab = 9;
                showLoader();
                sendReq(song_name, artist_name, song_image, song_audio, artist_list);
            }

        });
    }

    var closebtns = document.getElementById("close");

    closebtns.addEventListener("click", function() {
        this.parentElement.style.display = 'none';
        let background = document.getElementById("lyrics_bg");
            background.style.filter = 'none';
    });

    var favbtn = document.getElementById("fav_btn");

    favbtn.addEventListener("click", function (){
        this.style.color = 'gold';

        const url = '/addtofav/' + selected_tab;
        window.fetch(url);
    });

    var closebtns = document.getElementById("close_err");

    closebtns.addEventListener("click", function() {
        this.parentElement.style.display = 'none';
        let background = document.getElementById("lyrics_bg");
            background.style.filter = 'none';
    });

};
