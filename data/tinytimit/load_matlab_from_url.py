# small python routine to read this data over URL
#
# usage:
#   matdata = load_matlab_from_url("..../male-female.dat")
#   datam = matdata

def load_matlab_from_url(url):
    url_response = urllib.request.urlopen(url)
    matio = io.BytesIO(url_response.read())
    contents = sio.loadmat(matio,squeeze_me=True)
    return(contents)