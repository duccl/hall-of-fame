let id_display_search = '#search_results'
const callAPI = (text, callback) => {
    $.ajax({
        url: '/video/search',
        data: {
            'search_term': text
        },
        dataType: 'json'
    })
    .done(callback)
}

const populateSearchContainer =  (data) => {
    $(id_display_search).text(JSON.stringify(data))
}

let delayTimer;
$("#id_search_term").keyup(function(){
    clearTimeout(delayTimer);
    let search_text = $(this).val()
    $(id_display_search).text('Loading...')
    delayTimer = setTimeout(function(){
        callAPI(search_text,populateSearchContainer)
    },1000)
});