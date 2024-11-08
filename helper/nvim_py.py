# import pynvim
#
# # Connect to a running Neovim instance using an existing address
# # nvim = pynvim.attach('socket', path='/tmp/nvim')  # Change the path to your actual socket path
# # Or attach to an embedded Neovim instance (for running as a subprocess)
# nvim = pynvim.attach('child', argv=["nvim", "--embed"])
#
# # Now, you can interact with Neovim. For example:
# # Get the current buffer content
# buffer = nvim.current.buffer
# # print("Current buffer lines:", buffer[:])
#
# # Set some text in the current buffer
# buffer[0] = "Hello, Neovim from Python!"
#
# # Execute a Neovim command
# nvim.command("echo 'This is executed from Python!'")
#
# # Get and set variables in Neovim
# nvim.vars["my_var"] = "Python says hi"
# # print("Variable from Neovim:", nvim.vars["my_var"])
#
# # Close the connection
# nvim.close()
import pynvim

# Define a plugin class with the @pynvim.plugin decorator
@pynvim.plugin
class MyPlugin:
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('HelloCommand', nargs='*')
    def hello_command(self, args):
        self.nvim.out_write("Hello from Python!\n")

    @pynvim.function('MyFunction', sync=True)
    def my_function(self, args):
        return 'Hello, ' + args[0]

    @pynvim.autocmd('BufWritePost', pattern='*.py', sync=True)
    def on_buf_write_post(self):
        self.nvim.out_write("Python file saved!\n")

# let g:python3_host_prog = '/usr/bin/python3'
