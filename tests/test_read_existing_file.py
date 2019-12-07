from pituo.pituo import pituo


@pituo
def read_file_contents(fname):
    with open(fname) as f:
        return f.read()


content, err = read_file_contents('tests/existing_file.txt')

if err is not None:
    print(err)
else:
    print(content)
