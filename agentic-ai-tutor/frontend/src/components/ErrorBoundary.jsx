import { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, info) {
    console.error('[ErrorBoundary] caught error:', error, info?.componentStack);
  }

  handleReload = () => {
    this.setState({ hasError: false, error: null });
  };

  render() {
    if (!this.state.hasError) {
      return this.props.children;
    }

    return (
      <div
        className="flex flex-col items-center justify-center h-full gap-4 p-8 text-center"
        style={{ color: 'var(--text-secondary)' }}
      >
        <div className="text-4xl">&#9888;</div>
        <h2 className="text-lg font-semibold" style={{ color: 'var(--text-primary)' }}>
          Something went wrong
        </h2>
        <p className="text-sm max-w-md">An unexpected error occurred in this panel.</p>
        <button
          onClick={this.handleReload}
          className="px-4 py-2 text-sm rounded-lg border cursor-pointer"
          style={{
            borderColor: 'var(--accent)',
            color: 'var(--accent)',
            background: 'transparent',
          }}
        >
          Reload
        </button>
      </div>
    );
  }
}

export default ErrorBoundary;
