from pituo.pituo import pituo


def read_file_contents(fname):
    with open(fname) as f:
        return f.read()


read_file_contents = pituo(read_file_contents)

content, err = read_file_contents('nonexistent.txt')

if err is not None:
    print(err)
else:
    print(content)
