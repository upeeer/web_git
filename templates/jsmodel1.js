function reaction()
{
    let age_re=document.getElementById('age').value;
    let name_re=document.getElementById('name').value;
    let name_re=document.getElementById('sex').value;
    let marry_re=document.getElementById('ismarry').value;

    if(marry_re)
    {
        if(document.getElementById('male').checked())
            let marry_pr="先生"
        if(document.getElementById('female').checked())
            let marry_pr="女士"
    }
    else{
        if(document.getElementById('male').checked())
            let marry_pr="小帅哥"
        if(document.getElementById('female').checked())
            let marry_pr=""
    }


}
