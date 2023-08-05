ALLOWED_EXTENSIONS = ['csv']
UPLOADS_FOLDER = 'upload/'
def file_valid(file):
  return '.' in file and \
    file.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS