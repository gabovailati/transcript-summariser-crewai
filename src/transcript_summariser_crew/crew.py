from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq

@CrewBase
class TranscriptSummariserCrew():
	"""TranscriptSummariserCrew crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self) -> None:
		self.groq_llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config = self.agents_config['researcher'],
			llm = self.groq_llm
		)

	@agent
	def summariser(self) -> Agent:
		return Agent(
			config = self.agents_config['summariser'],
			llm = self.groq_llm
		)

	@task
	def find_transcripts_task(self) -> Task:
		return Task(
			config = self.tasks_config['find_transcripts_task'],
			agent = self.researcher()
		)

	@task
	def summarise_transcripts_task(self) -> Task:
		return Task(
			config = self.tasks_config['summarise_transcripts_task'],
			agent = self.summariser()
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the TranscriptSummariserCrew crew"""
		return Crew(
			agents =  self.agents,
			tasks = self.tasks,
			process = Process.sequential,
			verbose = 2
		)