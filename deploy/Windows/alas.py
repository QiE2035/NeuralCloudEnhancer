import time
import typing as t

from deploy.Windows.config import DeployConfig
from deploy.Windows.logger import logger
from deploy.Windows.utils import *


class AlasManager(DeployConfig):
    @cached_property
    def alas_folder(self):
        return [
            self.filepath(self.PythonExecutable),
            self.root_filepath
        ]

    @cached_property
    def self_pid(self):
        return os.getpid()

    def list_process(self) -> t.List[DataProcessInfo]:
        logger.info('List process')
        process = list(iter_process())
        logger.info(f'Found {len(process)} processes')
        return process

    def iter_process_by_names(self, names, in_alas=False) -> t.Iterable[DataProcessInfo]:
        """
        Args:
            names (str, list[str]): process name, such as 'alas.exe'
            in_alas (bool): If the output process must in Alas

        Yields:
            DataProcessInfo:
        """
        if not isinstance(names, list):
            names = [names]
        try:
            for proc in self.list_process():

                if not (proc.name and proc.name in names):
                    continue
                if proc.pid == self.self_pid:
                    continue
                if in_alas:
                    for folder in self.alas_folder:
                        if folder in proc.cmdline:
                            yield proc
                else:
                    yield proc
        except Exception as e:
            logger.info(str(e))
            return False

    def kill_process(self, process: DataProcessInfo):
        self.execute(f'taskkill /f /t /pid {process.pid}', allow_failure=True, output=False)

    def alas_kill(self):
        while 1:
            logger.hr(f'Kill existing Alas', 0)
            proc_list = list(self.iter_process_by_names(['alas.exe', 'python.exe'], in_alas=True))
            if not len(proc_list):
                break
            for proc in proc_list:
                logger.info(proc)
                self.kill_process(proc)


if __name__ == '__main__':
    self = AlasManager()
    start = time.time()
    self.alas_kill()
    print(time.time() - start)
