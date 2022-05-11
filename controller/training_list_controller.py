from Class import TrainingList, URL


def request_training_list(url: URL):
    tl = TrainingList()
    tl.set_traininig_list(url.get_response())
    return tl
